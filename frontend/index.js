const tag = document.getElementById('list');
async function getdata(){
    const data =await fetch('http://127.0.0.1:5000/users').then((data)=>data.json());
   return data;
}



getdata().then((data)=>{
  console.log(data);

  const html = data.map((user)=>{
    return `<li style="color:red">${user.email}-${user.address}</li>`
  }).join('')

  tag.innerHTML= html;


});