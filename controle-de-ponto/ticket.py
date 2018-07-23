import argparse
import datetime

from google.cloud import datastore
from google.cloud import storage


def create_datastore_client(project_id):
    return datastore.Client(project_id)


def create_storage_client(project_id):
    return storage.Client(project_id)


def add_ticket(client, *args, **kwargs):
    key = client.key('Ticket')

    ticket = datastore.Entity(
        key, exclude_from_indexes=['local', 'empresa', 'pessoa'])

    ticket.update({
        'created_at': datetime.datetime.utcnow(),
        'empresa': kwargs.get('empresa'),
        'local': kwargs.get('local'),
        'pessoa': kwargs.get('pessoa'),
        'date': kwargs.get('date'),
        'time': kwargs.get('time'),
        'done': False
    })

    client.put(ticket)

    return ticket.key


def get_today_start_time(client):
    today = "{day}/{month}".format(day=datetime.datetime.now().day, month=datetime.datetime.now().month)
    
    query = client.query(kind='Ticket')
    query.add_filter('date', '=', today)
    query.order = ['created_at']
    
    ticket = query.fetch(1)
    
    if not ticket:
    	return None

    return ticket


def mark_done(client, ticket_id):
    with client.transaction():
        key = client.key('Ticket', ticket_id)
        ticket = client.get(key)

        if not ticket:
            raise ValueError(
                'Ticket {} does not exist.'.format(ticket_id))

        ticket['done'] = True

        client.put(ticket)


def list_tickets(client):
    query = client.query(kind='Ticket')
    query.order = ['created_at']

    return list(query.fetch())


def delete_ticket(client, ticket_id):
    key = client.key('Ticket', ticket_id)
    client.delete(key)


def format_tickets(tickets):
    lines = []
    for ticket in tickets:
        if ticket['done']:
            status = 'done'
        else:
            status = 'created_at {}'.format(ticket['created_at'])

        lines.append('{}: {} ({})'.format(
            ticket['pessoa'], ticket['empresa'], status))

    return '\n'.join(lines)


def new_command(client, *kwargs):
    """Adds a ticket with kwargs."""
    ticket_key = add_ticket(client, *kwargs)
    print('Ticket {} added.'.format(ticket_key.id))


def done_command(client, args):
    """Marks a ticket as done."""
    mark_done(client, args.ticket_id)
    print('Ticket {} marked done.'.format(args.ticket_id))


def list_command(client, args):
    """Lists all tickets by creation time."""
    print(format_tickets(list_tickets(client)))


def delete_command(client, args):
    """Deletes a ticket."""
    delete_ticket(client, args.ticket_id)
    print('Ticket {} deleted.'.format(args.ticket_id))


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = create_storage_client('mycalendar-158220')
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser.add_argument('--project-id', help='Your cloud project ID.')

    new_parser = subparsers.add_parser('new', help=new_command.__doc__)
    new_parser.set_defaults(func=new_command)
    new_parser.add_argument('empresa', help='New ticket description.')

    done_parser = subparsers.add_parser('done', help=done_command.__doc__)
    done_parser.set_defaults(func=done_command)
    done_parser.add_argument('ticket_id', help='Ticket ID.', type=int)

    list_parser = subparsers.add_parser('list', help=list_command.__doc__)
    list_parser.set_defaults(func=list_command)

    delete_parser = subparsers.add_parser(
        'delete', help=delete_command.__doc__)
    delete_parser.set_defaults(func=delete_command)
    delete_parser.add_argument('ticket_id', help='Ticket ID.', type=int)

    args = parser.parse_args()

    datastore_client = create_datastore_client(args.project_id)
    
    args.func(datastore_client, args)