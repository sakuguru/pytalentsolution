from uuid import uuid4
from google.api_core.exceptions import InvalidArgument

from pytalentsolution import (
                                CustomAttributes, 
                                EmploymentType, 
                                Job, 
                                JobQuery, 
                                RequestMetadata, 
                                CompensationInfo, 
                                CompensationEntry, 
                                CompensationRange,
                                Money,
                                DegreeType,
                                CTS_CompensationInfo,
                                # LocationFilters
                            )
# from google.cloud.talent_v4 import LocationFilters


def test_job_with_custom_attr(tenant, company):
    j = Job(
            company=company.name,
            requisition_id=uuid4().hex,
            title="engineer",
            description="implement system",
            custom_attributes={
                "tags": CustomAttributes(
                        string_values=["hello"],
                        filterable=True,
                        keyword_searchable=True
                ),
                "min_exp": CustomAttributes(
                        long_values=[20],
                        filterable=True,
                        keyword_searchable=True
                )
            },
            addresses=["333/99 Moo 9, Pattaya Beach Road, South Pattaya, Chonburi, Thailand, 20150"],
            language_code="en-US",
            compensation_info=CompensationInfo(
                entries=[
                    CompensationEntry(
                        unit=CTS_CompensationInfo.CompensationUnit.MONTHLY,
                        range_=CompensationRange(
                            min_compensation=Money(
                                currency_code="THB", units=20000
                                ),
                            max_compensation=Money(
                                currency_code="THB", units=30000
                                )
                            ),
                        ),
                        ]
                    ),
            degree_types=[DegreeType.BACHELORS_OR_EQUIVALENT],
            )

    j3 = Job(
            company=company.name,
            requisition_id=uuid4().hex,
            title="worker",
            description="implement system",
            custom_attributes={
                "tags": CustomAttributes(
                        string_values=["hello"],
                        filterable=True,
                        keyword_searchable=True
                ),
                "min_exp": CustomAttributes(
                        long_values=[20],
                        filterable=True,
                        keyword_searchable=True
                )
            },
            addresses=["333/99 Moo 9, Pattaya Beach Road, North Pattaya, Chonburi, Thailand, 20150"],
            language_code="en-US",
            compensation_info=CompensationInfo(
                entries=[
                    CompensationEntry(
                        unit=CTS_CompensationInfo.CompensationUnit.MONTHLY,
                        range_=CompensationRange(
                            min_compensation=Money(
                                currency_code="THB", units=20000
                                ),
                            max_compensation=Money(
                                currency_code="THB", units=30000
                                )
                            ),
                        ),
                        ]
                    ),
            employment_types = [EmploymentType.PART_TIME],
            degree_types=[DegreeType.BACHELORS_OR_EQUIVALENT],
            )

    j4 = Job(
            company=company.name,
            requisition_id=uuid4().hex,
            title="worker",
            description="implement software",
            custom_attributes={
                "tags": CustomAttributes(
                        string_values=["hello"],
                        filterable=True,
                        keyword_searchable=True
                ),
                "min_exp": CustomAttributes(
                        long_values=[20],
                        filterable=True,
                        keyword_searchable=True
                )
            },
            addresses=["333/99 Moo 9, Pattaya Beach Road, South Pattaya, Chonburi, Thailand, 20150"],
            language_code="en-US",
            compensation_info=CompensationInfo(
                entries=[
                    CompensationEntry(
                        unit=CTS_CompensationInfo.CompensationUnit.MONTHLY,
                        range_=CompensationRange(
                            min_compensation=Money(
                                currency_code="THB", units=20000
                                ),
                            max_compensation=Money(
                                currency_code="THB", units=30000
                                )
                            ),
                        ),
                        ]
                    ),
            employment_types = [EmploymentType.PART_TIME],
            degree_types=[DegreeType.BACHELORS_OR_EQUIVALENT],
            )
    j5 = Job(
            company=company.name,
            requisition_id=uuid4().hex,
            title="worker",
            description="ผู้ใช้แรงงาน",
            custom_attributes={
                "tags": CustomAttributes(
                        string_values=["hello"],
                        filterable=True,
                        keyword_searchable=True
                ),
                "min_exp": CustomAttributes(
                        long_values=[20],
                        filterable=True,
                        keyword_searchable=True
                )
            },
            addresses=["333/99 Moo 9, Pattaya Beach Road, South Pattaya, Chonburi, Thailand, 20150"],
            language_code="en-US",
            compensation_info=CompensationInfo(
                entries=[
                    CompensationEntry(
                        unit=CTS_CompensationInfo.CompensationUnit.MONTHLY,
                        range_=CompensationRange(
                            min_compensation=Money(
                                currency_code="THB", units=20000
                                ),
                            max_compensation=Money(
                                currency_code="THB", units=30000
                                )
                            ),
                        ),
                        ]
                    ),
            degree_types=[DegreeType.BACHELORS_OR_EQUIVALENT],
            )
    j6 = Job(
            company=company.name,
            requisition_id=uuid4().hex,
            title="co-worker",
            description="labour",
            custom_attributes={
                "tags": CustomAttributes(
                        string_values=["hello"],
                        filterable=True,
                        keyword_searchable=True
                ),
                "min_exp": CustomAttributes(
                        long_values=[20],
                        filterable=True,
                        keyword_searchable=True
                )
            },
            addresses=["333/99 Moo 9, Pattaya Beach Road, South Pattaya, Chonburi, Thailand, 20150"],
            language_code="en-US",
            compensation_info=CompensationInfo(
                entries=[
                    CompensationEntry(
                        unit=CTS_CompensationInfo.CompensationUnit.MONTHLY,
                        range_=CompensationRange(
                            min_compensation=Money(
                                currency_code="THB", units=20000
                                ),
                            max_compensation=Money(
                                currency_code="THB", units=30000
                                )
                            ),
                        ),
                        ]
                    ),
            degree_types=[DegreeType.BACHELORS_OR_EQUIVALENT],
            )
    j7 = Job(
            company=company.name,
            requisition_id=uuid4().hex,
            title="worker",
            description="construction",
            custom_attributes={
                "tags": CustomAttributes(
                        string_values=["hello"],
                        filterable=True,
                        keyword_searchable=True
                ),
                "min_exp": CustomAttributes(
                        long_values=[20],
                        filterable=True,
                        keyword_searchable=True
                )
            },
            addresses=["333/99 Moo 9, Pattaya Beach Road, South Pattaya, Chonburi, Thailand, 20150"],
            language_code="en-US",
            compensation_info=CompensationInfo(
                entries=[
                    CompensationEntry(
                        unit=CTS_CompensationInfo.CompensationUnit.MONTHLY,
                        range_=CompensationRange(
                            min_compensation=Money(
                                currency_code="THB", units=20000
                                ),
                            max_compensation=Money(
                                currency_code="THB", units=30000
                                )
                            ),
                        ),
                        ]
                    ),
            degree_types=[DegreeType.BACHELORS_OR_EQUIVALENT],
            )
    j8 = Job(
            company=company.name,
            requisition_id=uuid4().hex,
            title="worker",
            description="ผู้ใช้แรงงาน",
            custom_attributes={
                "tags": CustomAttributes(
                        string_values=["hello"],
                        filterable=True,
                        keyword_searchable=True
                ),
                "min_exp": CustomAttributes(
                        long_values=[20],
                        filterable=True,
                        keyword_searchable=True
                )
            },
            addresses=["333/99 Moo 9, Pattaya Beach Road, South Pattaya, Chonburi, Thailand, 20150"],
            language_code="en-US",
            compensation_info=CompensationInfo(
                entries=[
                    CompensationEntry(
                        unit=CTS_CompensationInfo.CompensationUnit.MONTHLY,
                        range_=CompensationRange(
                            min_compensation=Money(
                                currency_code="THB", units=20000
                                ),
                            max_compensation=Money(
                                currency_code="THB", units=30000
                                )
                            ),
                        ),
                        ]
                    ),
            degree_types=[DegreeType.BACHELORS_OR_EQUIVALENT],
            )

    j9 = Job(
            company=company.name,
            requisition_id=uuid4().hex,
            title="Worker",
            description="factory",
            custom_attributes={
                "tags": CustomAttributes(
                        string_values=["hello"],
                        filterable=True,
                        keyword_searchable=True
                ),
                "min_exp": CustomAttributes(
                        long_values=[20],
                        filterable=True,
                        keyword_searchable=True
                )
            },
            addresses=["333/99 Moo 9, Pattaya Beach Road, South Pattaya, Chonburi, Thailand, 20150"],
            language_code="en-US",
            compensation_info=CompensationInfo(
                entries=[
                    CompensationEntry(
                        unit=CTS_CompensationInfo.CompensationUnit.MONTHLY,
                        range_=CompensationRange(
                            min_compensation=Money(
                                currency_code="THB", units=20000
                                ),
                            max_compensation=Money(
                                currency_code="THB", units=30000
                                )
                            ),
                        ),
                        ]
                    ),
            degree_types=[DegreeType.BACHELORS_OR_EQUIVALENT],
            )   
    j10 = Job(
            company=company.name,
            requisition_id=uuid4().hex,
            title="worker",
            description="production",
            custom_attributes={
                "tags": CustomAttributes(
                        string_values=["hello"],
                        filterable=True,
                        keyword_searchable=True
                ),
                "min_exp": CustomAttributes(
                        long_values=[20],
                        filterable=True,
                        keyword_searchable=True
                )
            },
            addresses=["333/99 Moo 9, Pattaya Beach Road, South Pattaya, Chonburi, Thailand, 20150"],
            language_code="en-US",
            compensation_info=CompensationInfo(
                entries=[
                    CompensationEntry(
                        unit=CTS_CompensationInfo.CompensationUnit.MONTHLY,
                        range_=CompensationRange(
                            min_compensation=Money(
                                currency_code="THB", units=20000
                                ),
                            max_compensation=Money(
                                currency_code="THB", units=30000
                                )
                            ),
                        ),
                        ]
                    ),
            degree_types=[DegreeType.BACHELORS_OR_EQUIVALENT],
            )         
    j.create(tenant=tenant)
    j3.create(tenant=tenant)
    j4.create(tenant=tenant)
    j5.create(tenant=tenant)
    j6.create(tenant=tenant)
    j7.create(tenant=tenant)
    j8.create(tenant=tenant)
    j9.create(tenant=tenant)
    j10.create(tenant=tenant)

    """ Update Job """
    j.title = "worker"
    j.employment_types = [EmploymentType.PART_TIME]
    j.custom_attributes.update({
                "tags_v1": CustomAttributes(
                        string_values=["hello"],
                        filterable=True,
                        keyword_searchable=True
                ),
                "min_exp_v2": CustomAttributes(
                        long_values=[20],
                        filterable=True,
                        keyword_searchable=True
                )})
    j.update()

    j2 = Job.get(name=j.name)
    assert j2.title == j.title
    assert j2.employment_types == j.employment_types


    """ Search Query """
    job_query_obj = JobQuery(
                        query="worker",
                        query_language_code= "en-US",
                        language_codes=["th-TH","en-US"],
                        location_filters=[{"address" : "chonburi","region_code":"TH"},{"address" : "bangkok","region_code":"TH"}],
                        employment_types=[EmploymentType.FULL_TIME]
                        )

    request_metadata_obj = RequestMetadata(domain="pytalentsolution", session_id="1", user_id="tester")
    result = Job.search_jobs(tenant=tenant, job_query=job_query_obj, request_metadata=request_metadata_obj)
    assert 'matching_jobs' not in result

    job_query_obj = JobQuery(
                        query="worker",
                        query_language_code= "en-US",
                        language_codes=["th-TH","en-US"],
                        location_filters=[{"address" : "bangkok","region_code":"TH"}],
                        employment_types=[EmploymentType.PART_TIME]
                        )

    request_metadata_obj = RequestMetadata(domain="pytalentsolution", session_id="1", user_id="tester")
    result = Job.search_jobs(tenant=tenant, job_query=job_query_obj, request_metadata=request_metadata_obj)
    assert 'matching_jobs' not in result

    job_query_obj = JobQuery(
                        query="worker",
                        query_language_code= "en-US",
                        language_codes=["th-TH","en-US"],
                        location_filters=[{"address" : "chonburi","region_code":"TH"}],
                        employment_types=[EmploymentType.PART_TIME]
                        )

    request_metadata_obj = RequestMetadata(domain="pytalentsolution", session_id="1", user_id="tester")
    result = Job.search_jobs(tenant=tenant, job_query=job_query_obj, request_metadata=request_metadata_obj)
    assert result['matching_jobs'] is not None

    job_query_obj = JobQuery(
                        query="worker",
                        query_language_code= "en-US",
                        language_codes=["th-TH","en-US"],
                        location_filters=[{"address" : "chonburi","region_code":"TH"}],
                        employment_types=[EmploymentType.PART_TIME]
                        )

    request_metadata_obj = RequestMetadata(domain="pytalentsolution", session_id="1", user_id="tester")
    result = Job.search_jobs(tenant=tenant, job_query=job_query_obj, request_metadata=request_metadata_obj)
    assert result['matching_jobs'] is not None

    job_query_obj = JobQuery(
                        query="worker",
                        query_language_code= "en-US",
                        language_codes=["th-TH","en-US"],
                        location_filters=[{"address" : "chonburi","region_code":"TH"}],
                        employment_types=[EmploymentType.PART_TIME]
                        )

    request_metadata_obj = RequestMetadata(domain="pytalentsolution", session_id="2", user_id="tester_2")
    result = Job.search_jobs(tenant=tenant, job_query=job_query_obj, request_metadata=request_metadata_obj, max_page_size=2)
    if result['next_page_token']:
        next_result = Job.search_jobs(tenant=tenant, 
                                    job_query=job_query_obj,
                                    next_page_token=result['next_page_token'],
                                    request_metadata=request_metadata_obj, 
                                    max_page_size=2)
        assert next_result is not None
        assert 'next_page_token' not in next_result.keys()  
    assert result['matching_jobs'] is not None

    job_query_obj = JobQuery(
                        query="worker",
                        query_language_code= "en-US",
                        language_codes=["th-TH","en-US"],
                        location_filters=[{"address" : "chonburi","region_code":"TH"}],
                        )

    request_metadata_obj = RequestMetadata(domain="pytalentsolution", session_id="2", user_id="tester_2")
    result = Job.search_jobs(tenant=tenant, 
                            job_query=job_query_obj, 
                            request_metadata=request_metadata_obj, 
                            max_page_size=5,
                            offset=5)
    assert len(result['matching_jobs']) == 4

    job_query_obj = JobQuery(
                        query="worker",
                        query_language_code= "en-US",
                        language_codes=["th-TH","en-US"],
                        location_filters=[{"address" : "chonburi","region_code":"TH"}],
                        )

    request_metadata_obj = RequestMetadata(domain="pytalentsolution", session_id="2", user_id="tester_2")
    result = Job.search_jobs(tenant=tenant, 
                            job_query=job_query_obj, 
                            request_metadata=request_metadata_obj, 
                            max_page_size=5,
                            offset=0)
    assert 'next_page_token' in result.keys()  
    assert result['matching_jobs'] is not None

    job_query_obj = JobQuery(
                        query="worker",
                        query_language_code= "en-US",
                        language_codes=["th-TH","en-US"],
                        location_filters=[{"address" : "chonburi","region_code":"TH"}],
                        )

    request_metadata_obj = RequestMetadata(domain="pytalentsolution", session_id="2", user_id="tester_2")
    result = Job.search_jobs(tenant=tenant, 
                            job_query=job_query_obj, 
                            request_metadata=request_metadata_obj, 
                            max_page_size=3)
    if result['next_page_token']:
        next_result = Job.search_jobs(tenant=tenant, 
                                    job_query=job_query_obj,
                                    next_page_token=result['next_page_token'],
                                    request_metadata=request_metadata_obj, 
                                    max_page_size=3,
                                    offset=2)
        assert len(next_result['matching_jobs']) == 3
        assert next_result is not None
        assert 'next_page_token' in next_result.keys()  
    assert result['matching_jobs'] is not None


    j.delete()
    j3.delete()
    j4.delete()
    j5.delete()
    j6.delete()
    j7.delete()
    j8.delete()
    j9.delete()
    j10.delete()




def test_job_with_fail_error(tenant, company):
    j = Job(
            company=company.name,
            requisition_id=uuid4().hex,
            title="engineer",
            description="implement system",
            custom_attributes={
                "tags": CustomAttributes(
                        string_values=["hello"],
                        filterable=True,
                        keyword_searchable=True
                ),
                "min_exp": CustomAttributes(
                        long_values=[20],
                        filterable=True,
                        keyword_searchable=True
                )
            },
            addresses=["12/12-23 dodo street"],
            language_code="en-US",
            compensation_info=CompensationInfo(
                entries=[
                    CompensationEntry(
                        unit=CTS_CompensationInfo.CompensationUnit.MONTHLY,
                        range_=CompensationRange(
                            min_compensation=Money(
                                currency_code="THB", units=20000
                                ),
                            max_compensation=Money(
                                currency_code="THB", units=30000
                                )
                            ),
                        ),
                        ]
                    ),
            degree_types=[DegreeType.BACHELORS_OR_EQUIVALENT],
            )

    try:
        x = j.create(tenant=tenant)
        j.delete()
    except InvalidArgument:
        print("\njob fail error")
