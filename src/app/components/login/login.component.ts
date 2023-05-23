import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  constructor(private router:Router){}
  loginUser(username:string,password:string){
    let reg_string=localStorage.getItem('registered_users');
    let reg:{username:string,password:string}[]=[];
    if(reg_string){
      reg=JSON.parse(reg_string);
    }
    const user=reg.find((userInfo:{username:string,password:string})=>userInfo.username==username && userInfo.password==password);
    if(!user){
      document.write("no user found");
    }
    else{
      console.log(user);
      this.router.navigateByUrl('./profile/')
      localStorage.setItem('loggedInUser',JSON.stringify(user));
    }
  }
}
