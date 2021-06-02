function CreatUsersList(users, first_name='', last_name='', email=''){
    console.log(users);
    const user = users[0];
    console.log(user);
    const curr_main = document.querySelector("main");
        for(let user of users){
            let section;
             // if (user.first_name === first_name || user.last_name === last_name || user.email === email || (first_name === '' & last_name === '' & email === ''))
                section = document.createElement('section');
                section.innerHTML=`
                    <img src="${user.avatar}" alt="profile picture"/>
                <div>
                    <span>${user.first_name} ${user.last_name}</span>
                    <br>
                        <a href="mailto:${user.email}">${user.email}</a>
                </div>`
                curr_main.appendChild(section);

        }

}
  let first_name = document.getElementsByName("username");
  let last_name = document.getElementsByName("lastname");
  let email = document.getElementsByName("email");
fetch('https://reqres.in/api/users?page=2').then(
    response=>response.json()
).then(
    responseOBJECT=>CreatUsersList(responseOBJECT.data, first_name,last_name,email)
)
    .catch(err => console.log(err));