function findMissingLetter(array) {
    var alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    var n = array[0];
    var x = array[array.length - 1];
    
    var n_ind = alfa.indexOf(n);
    var x_ind = alfa.indexOf(x);
    
    const newarr = alfa.slice(n_ind, x_ind+1);
    
    let combine = [...array, ...newarr];
    let excluded = combine.filter(el => {
      return !(array.includes(el) && newarr.includes(el));
    })
    return excluded.toString();
    
  }