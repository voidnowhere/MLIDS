import {Routes} from '@angular/router';
import {loggedOutGuard} from "./guards/logged-out.guard";

export const routes: Routes = [
  {
    path: 'home',
    loadComponent: () => import('./components/home/home.component').then(c => c.HomeComponent),
    title: 'Home',
  },
  {
    path: 'login',
    loadComponent: () => import('./components/login/login.component').then(c => c.LoginComponent),
    canActivate: [loggedOutGuard],
    title: 'Login',
  },
  {
    path: 'register',
    loadComponent: () => import('./components/register/register.component').then(c => c.RegisterComponent),
    canActivate: [loggedOutGuard],
    title: 'Register',
  },
];
