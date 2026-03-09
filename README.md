# API de Publicação de Tasks

Esta API foi desenvolvida em **Python** utilizando **FastAPI** com o objetivo de **receber requisições HTTP e publicar tasks em uma fila**, para que essas tasks sejam posteriormente consumidas e executadas por **workers**.

## Objetivo

A aplicação funciona como uma camada de entrada para disparo de processos assíncronos.  
Ela **não executa diretamente o processamento pesado**, mas apenas recebe os dados necessários, organiza o payload e envia a task para a fila configurada.

Os workers, em um serviço separado, são responsáveis por consumir essas mensagens e executar os fluxos correspondentes:
1 - Recuperar boletins de licitações
2 - Processar informações de licitações
3 - Comparar dados de licitações

---

## Tecnologias utilizadas

- **Python**
- **FastAPI**
- **Celery**
- **AMQP / AMQPS** para comunicação com a fila
- **Uvicorn** para execução da aplicação

---

## Como funciona

O fluxo da aplicação segue o padrão:

**Cliente HTTP → API FastAPI → Fila → Worker**

1. O cliente faz uma requisição para um dos endpoints disponíveis.
2. A API valida os dados recebidos.
3. A API publica uma task na fila configurada.
4. Um worker consome essa task e executa o processamento necessário.

---

## Endpoints disponíveis

A API possui atualmente os seguintes endpoints:

### `POST /bulletins`
Endpoint responsável por publicar tasks relacionadas ao processamento de boletins.

### `POST /bidding/info`
Endpoint responsável por publicar tasks relacionadas à coleta ou processamento de informações de licitações.

### `POST /bidding/compare`
Endpoint responsável por publicar tasks relacionadas à comparação de dados de licitações.

---

## Documentação da API

Como a aplicação foi construída com **FastAPI**, a documentação interativa dos endpoints fica disponível automaticamente.

Após subir a aplicação, a documentação pode ser acessada em:

### Swagger UI
`/docs`

Exemplo:
```text
http://localhost:8000/docs
