import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {env} from "../env";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class IdCardExtractorService {
  constructor(private http: HttpClient) {
  }

  public getDate(date: FormData): Observable<any> {
    return this.http.post(`${env.baseUrl}/extract`, date);
  }
}
