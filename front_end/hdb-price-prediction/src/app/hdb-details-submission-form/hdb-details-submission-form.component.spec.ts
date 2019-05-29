import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HdbDetailsSubmissionFormComponent } from './hdb-details-submission-form.component';

describe('HdbDetailsSubmissionFormComponent', () => {
  let component: HdbDetailsSubmissionFormComponent;
  let fixture: ComponentFixture<HdbDetailsSubmissionFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HdbDetailsSubmissionFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HdbDetailsSubmissionFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
