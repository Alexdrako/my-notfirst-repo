//const entrance = [4,4,8,3,3,3,2,4,4];

//entrance.forEach(item => console.log(item))

//for (var  = 0; i<entrance.length; i++){console.log(entrance[i])}

//for (var i = 0; i<3; i++){console.log(entrance[i])}

//let totalSum = 0; 
//for (let i = 0; i<entrance.length; i++) {
//  totalSum += entrance[i]; 
//}
//console.log("total sum:", totalSum);


//for (let i = 0; i < entrance.length; i++) {
 // if (entrance[i] !== 4) { 
//    totalSum += entrance[i]; // Якщо так, додаємо його до суми
//  }
//}
//console.log("sum expect 4's:", totalSum);

import {readFileSync} from 'fs';

var body = readFileSync('List.json','utf8');
const data = JSON.parse(body);
const lists = data.lists;

for (let i = 0; i<data.lists.length; i++)
console.log(lists[i].id, lists[i].name);