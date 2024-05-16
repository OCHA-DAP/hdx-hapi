-- dummy data
INSERT INTO dataset (hdx_id, hdx_stub, title, hdx_provider_stub, hdx_provider_name)
VALUES
('90deb235-1bf5-4bae-b231-3393222c2d01', 'dataset01', 'Dataset #1', 'provider01', 'Provider #1'),
('b9e438e0-b68a-49f9-b9a9-68c0f3e93604', 'dataset02', 'Dataset #2', 'provider02', 'Provider #2'),
('62ad6e55-5f5d-4494-854c-4110687e9e25', 'dataset03', 'Dataset #3', 'provider03', 'Provider #3');

-- dummy data
INSERT INTO resource (hdx_id, dataset_hdx_id, name, format, update_date, is_hxl, download_url, hapi_updated_date)
VALUES
('17acb541-9431-409a-80a8-50eda7e8ebab', '90deb235-1bf5-4bae-b231-3393222c2d01', 'resource-01.csv', 'csv', '2023-06-01 00:00:00',TRUE,
'https://data.humdata.org/dataset/c3f001fa-b45b-464c-9460-1ca79fd39b40/resource/90deb235-1bf5-4bae-b231-3393222c2d01/download/resource-01.csv',
  '2023-01-01 00:00:00'),
('d1160fa9-1d58-4f96-9df5-edbff2e80895', 'b9e438e0-b68a-49f9-b9a9-68c0f3e93604','resource-02.xlsx', 'xlsx', '2023-07-01 00:00:00',TRUE,
'https://fdw.fews.net/api/tradeflowquantityvaluefacts/?dataset=1845&country=TZ&fields=simple&format=xlsx',
  '2023-01-01 00:00:00'),
('a8e69c6c-16fc-4983-92ee-e04e8960b51f', '62ad6e55-5f5d-4494-854c-4110687e9e25', 'resource-03.csv', 'csv', '2023-08-01 00:00:00',TRUE, 
 'https://data.humdata.org/dataset/7cf3cec8-dbbc-4c96-9762-1464cd0bff75/resource/62ad6e55-5f5d-4494-854c-4110687e9e25/download/resource-03.csv',
 '2023-01-01 00:00:00');
