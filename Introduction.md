# Introdução
Gostaria de ler as informações de textos a partir de fotos (imagem) usando OCR, identificar os dados necessários e salvar no banco de dados.
Com isso poderia gerar dados mais específicos e precisos para facilitar as tomadas de decisões.

# Objetivo
Dividi em três objetivos principais:

1) Analise da foto de um ticket, cupom fiscal ou registro de ponto e guardamos as informações em um banco de dados não relacional;
	Conseguir através da foto, ler os textos e guardar as informações relevantes no banco de dados.

2) Analise das informações;
	Entregar informação, filtrada, para tomada de decisões.

3) Demonstrar em gráficos as informações.

# Casos de uso
Foram identificados os seguintes casos de uso:

## Controle de compras
Você precisa ter controle sobre a compra de cada produto ou serviço. Por exemplo, você sabe quanto gastou com presunto no mês passado? Ou quanto foi a variação do preço do feijão em determinado período?

## Controle de ponto pessoal
Você quer controlar suas horas de trabalho. Ter acesso a uma tabela com as horas e receber alertas para a hora do almoço, o tempo de intervalo ou a hora da saída.

### Informações dos tickets
O ticket deve ter alguns requisitos dependendo do tipo caso de uso.
São necessárias certas informações para que funcione da maneira adequada. Por exemplo, para o **controle de ponto pessoal** precisamos das seguintes informações no ticket: `empresa`, `local`, `pessoa`, `data` e `hora`.