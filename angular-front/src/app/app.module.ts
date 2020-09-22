import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';

// import {
//   Configuration as ConfigurationUser,
//   ConfigurationParameters as ConfigurationParametersUser,
//   ApiModule as ApiModuleUser
// } from './shared/services/user-service';
// import { environment } from 'src/environments/environment';

// export function userServicefactory(): ConfigurationUser {
//   const params: ConfigurationParametersUser = {
//     'basePath': environment.API_USER_URL
//   };
//   return new ConfigurationUser(params);
// }

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule //,
    //ApiModuleUser.forRoot(userServicefactory)
  ],
  providers: [
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
