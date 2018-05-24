/*

Write a JavaScript program to perform a binary search.

*/

function binary_Search(items, value){
    var lIndex  = 0,
        rIndex   = items.length - 1,
        midIndex = Math.floor((rIndex + lIndex)/2);

    while(items[midIndex] != value && lIndex < rIndex){
       if (value < items[midIndex]){
            rIndex = midIndex - 1;
        } 
      else if (value > items[midIndex]){
            lIndex = midIndex + 1;
        }
        midIndex = Math.floor((rIndex + lIndex)/2);
    }

 return (items[midIndex] != value) ? -1 : midIndex;
}

var items = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91];
searchedIdx = binary_Search(items, 23)
if (searchedIdx != -1){
    console.log("Number found at "+ searchedIdx);  
} else {
    console.log("Number not found")
}
 