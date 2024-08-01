function inArray(array1,array2){
    var r = array1.filter(word => array2.some(checkword => checkword.includes(word))).sort();
    return r;
  }