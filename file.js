import React, { useState, useEffect, useRef } from 'react';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { Toast } from 'primereact/toast';
import { CustomerService } from '../service/CustomerService';
import './DataTableDemo.css';

const DataTableRowGroupDemo = () => {

    const [customers, setCustomers] = useState([]);
    const [expandedRows, setExpandedRows] = useState([]);
    const toast = useRef(null);
    const customerService = new CustomerService();

    useEffect(() => {
        customerService.getCustomersMedium().then(data => setCustomers(data));
    }, []); // eslint-disable-line react-hooks/exhaustive-deps

    const headerTemplate = (data) => {
        return (
            <React.Fragment>
                <img alt={data.representative.name} src={`images/avatar/${data.representative.image}`} onError={(e) => e.target.src = 'https://www.primefaces.org/wp-content/uploads/2020/05/placeholder.png'} width="32" style={{ verticalAlign: 'middle' }} />
                <span className="image-text">{data.representative.name}</span>
            </React.Fragment>
        );
    }

    const footerTemplate = (data) => {
        return (
            <React.Fragment>
                <td colSpan="4" style={{ textAlign: 'right' }}>Total Customers</td>
                <td>{calculateCustomerTotal(data.representative.name)}</td>
            </React.Fragment>
        );
    }

    const countryBodyTemplate = (rowData) => {
        return (
            <React.Fragment>
                <img alt={rowData.country.name} src="/images/flag/flag_placeholder.png" onError={(e) => e.target.src = 'https://www.primefaces.org/wp-content/uploads/2020/05/placeholder.png'} className={`flag flag-${rowData.country.code}`} width="30" />
                <span className="image-text">{rowData.country.name}</span>
            </React.Fragment>
        );
    }

    const statusBodyTemplate = (rowData) => {
        return <span className={`customer-badge status-${rowData.status}`}>{rowData.status}</span>;
    }

    const representativeBodyTemplate = (rowData) => {
        return (
            <React.Fragment>
                <img alt={rowData.representative.name} src={`images/avatar/${rowData.representative.image}`} onError={(e) => e.target.src = 'https://www.primefaces.org/wp-content/uploads/2020/05/placeholder.png'} width="32" style={{ verticalAlign: 'middle' }} />
                <span className="image-text">{rowData.representative.name}</span>
            </React.Fragment>
        )
    }

    const onRowGroupExpand = (event) => {
        toast.current.show({ severity: 'info', summary: 'Row Group Expanded', detail: 'Value: ' + event.data.representative.name, life: 3000 });
    }

    const onRowGroupCollapse = (event) => {
        toast.current.show({ severity: 'success', summary: 'Row Group Collapsed', detail: 'Value: ' + event.data.representative.name, life: 3000 });
    }

    const calculateCustomerTotal = (name) => {
        let total = 0;

        if (customers) {
            for (let customer of customers) {
                if (customer.representative.name === name) {
                    total++;
                }
            }
        }

        return total;
    }

    return (
        <div className="datatable-rowgroup-demo">
            <Toast ref={toast}></Toast>

            <div className="card">
                <h5>Subheader Grouping</h5>
                <p>Group customers by their representative.</p>
                <DataTable value={customers} rowGroupMode="subheader" groupRowsBy="representative.name"
                    sortMode="single" sortField="representative.name" sortOrder={1} scrollable scrollHeight="400px"
                    rowGroupHeaderTemplate={headerTemplate} rowGroupFooterTemplate={footerTemplate} responsiveLayout="scroll">
                    <Column field="name" header="Name" style={{ minWidth: '200px' }}></Column>
                    <Column field="country" header="Country" body={countryBodyTemplate} style={{ minWidth: '200px' }}></Column>
                    <Column field="company" header="Company" style={{ minWidth: '200px' }}></Column>
                    <Column field="status" header="Status" body={statusBodyTemplate} style={{ minWidth: '200px' }}></Column>
                    <Column field="date" header="Date" style={{ minWidth: '200px' }}></Column>
                </DataTable>
            </div>

            <div className="card">
                <h5>Expandable Row Groups</h5>
                <p>Group customers by their representative.</p>
                <DataTable value={customers} rowGroupMode="subheader" groupRowsBy="representative.name"
                    sortMode="single" sortField="representative.name" sortOrder={1} responsiveLayout="scroll"
                    expandableRowGroups expandedRows={expandedRows} onRowToggle={(e) => setExpandedRows(e.data)}
                    onRowExpand={onRowGroupExpand} onRowCollapse={onRowGroupCollapse}
                    rowGroupHeaderTemplate={headerTemplate} rowGroupFooterTemplate={footerTemplate}>
                    <Column field="name" header="Name"></Column>
                    <Column field="country" header="Country" body={countryBodyTemplate}></Column>
                    <Column field="company" header="Company"></Column>
                    <Column field="status" header="Status" body={statusBodyTemplate}></Column>
                    <Column field="date" header="Date"></Column>
                </DataTable>
            </div>

            <div className="card">
                <h5>RowSpan Grouping</h5>
                <DataTable value={customers} rowGroupMode="rowspan" groupRowsBy="representative.name"
                    sortMode="single" sortField="representative.name" sortOrder={1} responsiveLayout="scroll">
                    <Column header="#" headerStyle={{ width: '3em' }} body={(data, options) => options.rowIndex + 1}></Column>
                    <Column field="representative.name" header="Representative" body={representativeBodyTemplate}></Column>
                    <Column field="name" header="Name"></Column>
                    <Column field="country" header="Country" body={countryBodyTemplate}></Column>
                    <Column field="company" header="Company"></Column>
                    <Column field="status" header="Status" body={statusBodyTemplate}></Column>
                    <Column field="date" header="Date"></Column>
                </DataTable>
            </div>
        </div>
    );
}