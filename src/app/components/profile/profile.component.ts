import { Component } from '@angular/core';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {
  data = JSON.parse(localStorage.getItem('loggedInUser')|| '{}')
  displayusername = this.data.username;
  displaypassword = this.data.password;
}
