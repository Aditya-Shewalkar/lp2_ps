import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})



export class RegisterComponent {

  registerUser(username:string,password:string){
    let register_string =localStorage.getItem("registered_users");
    let reg:{username:string,password:string}[]=[];
    if(register_string){
      reg=JSON.parse(register_string);
    }
    reg?.push({
      username:username,
      password:password
    })
    localStorage.setItem("registered_users",JSON.stringify(reg));
  }
}
