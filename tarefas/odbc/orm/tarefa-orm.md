### ODBC (Open Database Connectivity)

#### Descrição:
ODBC é uma interface de programação que permite que aplicativos acessem e manipulem dados em diversos sistemas de gerenciamento de banco de dados (SGBDs) de forma uniforme, independentemente do sistema operacional ou do SGBD utilizado.

#### Funcionamento:
1. **Driver ODBC:** Um driver ODBC é um componente de software que permite a comunicação entre o aplicativo e o SGBD.
2. **Conexão:** O aplicativo estabelece uma conexão com o SGBD através de um DSN (Data Source Name) configurado no sistema.
3. **Execução de Comandos SQL:** Uma vez estabelecida a conexão, o aplicativo pode enviar comandos SQL para o SGBD, como consultas de leitura, inserção, atualização ou exclusão de dados.
4. **Processamento de Resultados:** O SGBD executa as consultas e retorna os resultados para o aplicativo através do driver ODBC

#### Vantagens:
- **Portabilidade:** Permite que os aplicativos acessem uma variedade de SGBDs sem precisar modificar o código.
- **Padronização:** Oferece uma interface padronizada para acesso a dados, facilitando o desenvolvimento e a manutenção de aplicativos.
- **Performance:** Os drivers ODBC são otimizados para maximizar a performance de acesso aos dados.

### ORM (Object-Relational Mapping)

#### Descrição:
ORM é uma técnica de programação que mapeia objetos de um sistema orientado a objetos para tabelas em um banco de dados relacional, facilitando a interação entre o código da aplicação e o banco de dados.

#### Funcionamento:
1. **Mapeamento Objeto-Relacional:** Cada tabela do banco de dados é mapeada para uma classe e cada coluna é mapeada para uma propriedade (atributo) da classe.
2. **Operações CRUD:** O ORM fornece métodos para realizar operações CRUD (Create, Read, Update, Delete) nos objetos, que são traduzidas em consultas SQL pelo ORM e executadas no banco de dados.
3. **Relacionamentos:** O ORM permite definir e trabalhar com relacionamentos entre objetos, como associações um-para-um, um-para-muitos e muitos-para-muitos.
4. **Abstração do Banco de Dados:** Os desenvolvedores interagem com objetos em vez de tabelas e consultas SQL, tornando o código mais legível e fácil de manter.

#### Vantagens:
- **Produtividade:** Reduz a quantidade de código necessário para interagir com o banco de dados, acelerando o desenvolvimento.
- **Portabilidade:** Permite que o código da aplicação seja independente do SGBD subjacente, facilitando a migração entre sistemas de banco de dados.
- **Manutenção:** Simplifica a manutenção do código, pois as mudanças na estrutura do banco de dados podem ser refletidas automaticamente no mapeamento objeto-relacional.
