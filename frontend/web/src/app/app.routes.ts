import {Routes} from '@angular/router';
import {loggedOutGuard} from "./guards/logged-out.guard";
import {loggedInGuard} from "./guards/logged-in.guard";

export const routes: Routes = [
  {
    path: 'home',
    loadComponent: () => import('./components/home/home.component').then(c => c.HomeComponent),
    title: 'Home',
  },
  {
    path: 'extract',
    loadComponent: () => import('./components/extract/extract.component').then(c => c.ExtractComponent),
    canActivate: [loggedInGuard],
    title: 'Extract',
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
