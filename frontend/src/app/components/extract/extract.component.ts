import {Component} from '@angular/core';
import {FileUploadModule} from "primeng/fileupload";
import {PrimeIcons} from "primeng/api";
import {IdCardExtractorService} from "../../services/id-card-extractor.service";
import {ProgressSpinnerModule} from "primeng/progressspinner";

@Component({
  selector: 'app-extract',
  standalone: true,
  imports: [
    FileUploadModule,
    ProgressSpinnerModule
  ],
  templateUrl: './extract.component.html',
})
export class ExtractComponent {
  data: any = null;
  loading: boolean = false;

  constructor(private service: IdCardExtractorService) {
  }

  onSelectImage(event: any) {
    const file = event.target.files[0];
    let formDate = new FormData();
    formDate.append('file', file);
    this.loading = true;
    this.service.getDate(formDate).subscribe({
      next: (value: any) => {
        this.data = value;
        this.loading = false;
      },
    });
  }

  protected readonly PrimeIcons = PrimeIcons;
}
