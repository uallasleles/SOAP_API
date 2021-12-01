# SOAP API

Neste projeto implemento uma API baseada no protocolo SOAP.  
<br>

### Algumas definições importantes:  

## API

API é um conjunto de definições e protocolos usado no desenvolvimento e na integração de software de aplicações.
Ela simplifica a forma como os desenvolvedores integram novos componentes de aplicações a uma arquitetura preexistente.
Para manter a competitividade, é importante oferecer suporte à implantação e desenvolvimento rápidos de serviços inovadores.
As APIs são uma maneira simplificada de conectar a própria infraestrutura por meio do desenvolvimento de aplicações nativas em nuvem.
Elas também possibilitam o compartilhamento de dados com clientes e outros usuários externos.
Com as APIs, você libera o acesso aos seus recursos sem abrir mão da segurança e do controle.
É possível conectar APIs, bem como criar aplicações que fazem uso dos dados ou funcionalidades disponibilizadas por elas, usando uma plataforma de integração distribuída que ligue todos os elementos, incluindo sistemas legados e dispositivos de Internet das Coisas (IoT).

## SOAP

Uma especificação de protocolo foi desenvolvida para ajudar API's a padronizar a troca de informações: O *Simple Object Access Protocol*, mais conhecido como SOAP.
As APIs projetadas com SOAP usam o XML como formato de mensagem e recebem solicitações por HTTP ou SMTP.

Existem algumas bibliotecas Python que auxiliam no desenvolvimento de web services baseados em SOAP. Para implementar o Provedor de Serviços SOAP vamos utilizar o Spyne.

> Spyne é um kit de ferramentas Python RPC que facilita a exposição de serviços online que têm uma API bem definida usando vários protocolos e transportes. Ele é uma versão generalizada de uma biblioteca Soap conhecida como Soaplib.

Vale a pena visitar o site: [Spyne](http://spyne.io/)

## Flask App

Para interagir com nossa API vamos construir uma aplicação Flask básica, uma página HTML com um textbox e um button. O Flask depende do mecanismo de modelo Jinja e do kit de ferramentas Werkzeug WSGI.

## Werkzeug WSGI

Os serviços SOAP são aplicativos WSGI distintos, precisamos envolver os serviços SOAP com um middleware despachante de aplicativos para "reunir" todos os aplicativos em "um só".

- Middleware - Um Middleware WSGI é um aplicativo WSGI que envolve outro aplicativo para observar ou alterar seu comportamento. Werkzeug fornece alguns middlewares para casos de uso comuns, usaremos o Application Dispatcher (DispatcherMiddleware).

- Application Dispatcher - Este middleware (DispatcherMiddleware) cria um único aplicativo WSGI que despacha para vários outros aplicativos WSGI montados em diferentes caminhos de URL.

# Instalações

1. **Criar um ambiente virtual utilizando o Virtualenv**
    ```shell
    > virtualenv env
    > .\env\Scripts\activate
    ```
1. **Instalar o Flask**
    ```shell
    > pip install flask
    ```
    Após instalar o Flask, faça:
    ```shell 
    > flask --version
    ```
    Perceberá que o Werkzeug está instalado por padrão.

1. **Instalar o Spyne**
    ```shell
    > pip install spyne
    ```

1. **Instalar o requirements.txt**
    ```shell
    > pip install -r requirements.txt
    ```
___

### Referências:


`Virtualenv`  
[https://virtualenv.pypa.io/](https://virtualenv.pypa.io/)

`Flask`  
[https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

`Werkzeug`  
[https://werkzeug.palletsprojects.com/](https://werkzeug.palletsprojects.com/)

`Spyne`  
[http://spyne.io/](http://spyne.io/)