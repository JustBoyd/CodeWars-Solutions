function descendingOrder(n){
    if (n > 9){
      arr = Array.from(String(n), Number);
      sortedarr = arr.sort((a, b) => b-a);
      num = sortedarr.reduce((accum, digit) =>(accum * 10) + digit,0)
      return num;
    } else{
      return n;
    }
  }