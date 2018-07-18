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
Como você controla suas compras? Caso: Você vai a padaria, compra pão e outras coisas e acaba pagando em dinheiro.
No final do mês você consegue facilmente ter as informações detalhadas dos gastos? Por exemplo, você sabe quanto gastou com presunto no mês passado?
Usando o sistema você envia uma foto do cupom de compra, que contém as informações `local onde a compra foi feita` , `data em que foi feita`, `lista com preço dos produtos comprados`, `forma de pagamento` e `mais informações sobre pagamento` , o sistema lê o cupom e guarda essas informações para acesso futuro. Ao final do mês você consegue detalhar suas compras e saber onde gastou, como gastou e como pagou.

## Controle de ponto pessoal
Você quer controlar suas horas de trabalho, você bate ponto e recebe um registro de ponto impresso. Ao final do mês você precisa confrontar as horas na folha de pagamento.
Utilize o sistema enviando uma foto do registro de ponto, você poderá ver uma lista com seus horários e customizar dashboards. Além disso poderá criar notificações para `hora de almoço` e `hora de saída`.
