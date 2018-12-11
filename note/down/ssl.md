# ssl相关
- what is ssl:
  SSL (Secure Sockets Layer) is a standard security protocol for establishing encrypted links between a web server and a browser in an online communication.

  The usage of SSL technology ensures that all data transmitted between the web server and browser remains encrypted.

  An SSL certificate is necessary to create SSL connection. You would need to give all details about the identity of your website and your company as and when you choose to activate SSL on your web server. Following this, two cryptographic keys are created - a Private Key and a Public Key.
  总而言之,ssl就是对web和游览器的数据通信进行加密的协议
- 现在主流游览器不能打开没有ssl证书的网站
- ssl._create_default_https_context = ssl._create_unverified_context 利用非认证上下文环境替换认证的上下文环境(需要导入ssl包)
