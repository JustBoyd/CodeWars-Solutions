function domainName(url){
    var domain = url.replace(/.+\/\/|www.|\..+/g, '')
    return domain
  }