import {Component, OnInit, ViewChild} from '@angular/core';
import {FormioComponent} from 'angular-formio';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {map} from 'rxjs/operators';

@Component({
  selector: 'app-hdb-details-submission-form',
  templateUrl: './hdb-details-submission-form.component.html',
  styleUrls: ['./hdb-details-submission-form.component.scss']
})
export class HdbDetailsSubmissionFormComponent implements OnInit {

  @ViewChild('formioComponent')
  formioComponent: FormioComponent;

  prediction: string;
  isPredictionReturn = false;
  isRendered = false;
  public formJson: any;

  constructor(private httpClient: HttpClient) {
  }

  ngOnInit() {
    this.httpClient.get('assets/form-payload.json').subscribe(payload => {
      this.formJson = payload;
    });
  }

  submitValue($event: any) {
    this.clearAlerts();
    console.log($event.data);
    if (this.formioComponent.formio.checkValidity($event.data, true)) {
      const payload = this.marshallData($event.data);
      console.log('The payload is ', payload);
      this.getHousePricePrediction(payload).subscribe(prediction => {
        this.isPredictionReturn = true;
        this.prediction = prediction.toFixed(0);
        this.prediction = this.formatDataForDisplay(this.prediction);
      }, error => {
        console.error(error);
        this.formioComponent.alerts.setAlert({type: 'danger', message: error.message});
      });
    } else {
      this.isPredictionReturn = false;
      console.log('There is error');
    }
  }

  marshallData(input: any) {
    const ret = {};
    ret['town'] = [input['town']];
    ret['flat_type'] = [input['flat_type']];
    ret['storey_random'] = [input['floor']];
    ret['floor_area_sqm'] = [input['floor_area_sqm']];
    ret['flat_model'] = [input['flat_model']];
    ret['street_name'] = [''];
    ret['lease_commence_date'] = [input['lease_commence_date']];

    const formatDateToYearDay = (dateStr) => {
      const a_date = new Date(dateStr);
      return `${a_date.getFullYear()}-${a_date.getMonth() + 1}`;
    };
    ret['month'] = ['2017-05'];
    ret['block'] = [''];
    return {'payload': ret};
  }

  clearAlerts() {
    this.formioComponent.alerts.setAlerts([]);
  }

  getHousePricePrediction(payload: any): Observable<number> {
    return this.httpClient.post('http://34.87.108.41/hdb/predict', payload)
      .pipe(
        map((response: any) => {
          return response;
        })
      );
  }

  onRender() {
    this.isRendered = true;
  }

  private formatDataForDisplay(input: string) {
    return parseFloat(input).toLocaleString('en');
  }
}
