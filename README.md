### Crawler - Pague Menos

Esse projeto tem como finalizada extrair informações referente aos produtos disponíveis no site da [Farmácia Pague Menos](https://www.paguemenos.com.br/). Para isso, foi desenvolvido um crawler baseado na liguagem python com a ferramenta **Scrapy** .

O objetivo do crawler é extrair as seguintes informações para cada produto:
* EAN (ean)
* Nome do produto (name) 
* Preço (price)
* Moeda do preço (priceCurrency)
* Marca (brand)
* Cod. da Loja (sku)
* Departamento (categories)
* Vendedor (seller)
* Url da imagem do produto (imageUrl)
* Url do produto (productUrl)
* Validade da precificação (priceValidUntil)
* Data da extração (created_at)

Com esses dados podemos monitorar a validade das precificação de cada produto e realizar a rastreabilidade dessa informação via código EAN(global)/sku(ambiente e-commerce).  

### Especificações - site

O site da [Farmácia Pague Menos](https://www.paguemenos.com.br/) funciona no modelo de e-commerce e armazena a precificação via plataforma Vtex. Além disso, o site é baseado em JavaScript, portanto exige a interação com alguns elementos gráficos da página para realizar ações, por exemplo: carregar próximos produtos por meio do acionamento de um botão.

### Estratégia para raspagem

A estratégia para extrair os dados do site foi acessar o [Sitemaps](https://www.paguemenos.com.br/sitemap.xml) para acessar os setores/departamentos dos medicamentos. A paginação desses itens foi realizada com a manipulação da url base de cada departamento. Os dados extraídos são armazenados em formato *json* no diretório *raw*.

