function solution(numbers){
    if (!numbers || numbers.length === 0) {
      return "";
    }
    
    let result = [];
    let start = numbers[0];
    let end = numbers[0];
    
    for (let i = 1; i < numbers.length; i++) {
      if (numbers[i] === end + 1) {
        end = numbers[i];
      } else {
        if (end - start >= 2) {
          result.push(`${start}-${end}`);
        } else {
          for (let j = start ; j <= end; j++) {
            result.push(j.toString());
          }
        }
        start = end = numbers[i];
      }
    }
    
    if ( end - start >= 2) {
      result.push(`${start}-${end}`);
    } else {
      for (let j = start; j <= end; j++) {
        result.push(j.toString());
      }
    }
    
    return result.join(",");
    // TODO: complete solution 
  }