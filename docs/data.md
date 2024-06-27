
# Data Coverage

---

The initial aim of HDX HAPI is to cover all countries that have a
humanitarian response plan, and all data sub-categories from
[HDX data grids](https://data.humdata.org/dashboards/overview-of-data-grids).
In the table below we detail the sub-category coverage that we have achieved
at present, and to which administrative level: national (admin 0),
admin 1, or admin 2.

<style>
  .admin2 {
    background-color: #007CE0;
  }
  .admin1 {
    background-color: #66B0EC;
  }
  .admin0 {
    background-color: #CCE5F9;
  }
  .empty-cell {
    background-color: #FFF;
  }
  table {
    border-collapse: separate;
    width: 100%;
  }

  th, td {
    border-right: 1px solid #CCC;
    line-height: 16px;
    padding: 8px 12px;
    width: 200px;
  }

  thead th {
    background-color: #F2F2F2;
    border-bottom: 1px solid #CCC;
    border-top: 1px solid #CCC;
    position: sticky;
    top: 0;
    z-index: 2;
  }

  .fixed-col {
    background-color: #F2F2F2;
    border-left: 1px solid #CCC;
    font-weight: 700;
    position: -webkit-sticky;
    position: sticky;
    left: 0;
    z-index: 3;
  }

  tbody .fixed-col {
    z-index: 1;
  }

  tr > td.fixed-col {
    border-right: 1px solid #CCC;
  }
  thead > tr > th.fixed-col {
  	background-color: #FFF;
  	border-color: #FFF;
    border-right: 1px solid #CCC;
    border-bottom: 1px solid #CCC;
  }
  tbody tr:first-child td {
    border-top: 0 !important;
  }
  tbody tr:last-child td {
    border-bottom: 1px solid #CCC;
  }

  /** overrides **/
	.md-typeset__table {
		display: block;
    height: 800px;
		margin: 0;
    overflow: auto;
		padding: 0;
		position: relative;
    width: 100%;
	}
	.md-typeset__scrollwrap {
		margin: 0;
		overflow: hidden;
	}
	.md-typeset table:not([class]) {
		border: 0;
		display: unset;
		overflow: unset;
	}
	.md-typeset table:not([class]) td {
		border-color: #CCC;
		vertical-align: middle;
	}
	.md-typeset table:not([class]) th {
		vertical-align: bottom;
	}
</style>

<table>
  <thead>
    <tr>
      <th class="fixed-col"></th>
      <th>Refugees & Persons Of Concern</th>
      <th>Humanitarian Needs</th>
      <th>Who is Doing What Where - Operational Presence</th>
      <th>Funding</th>
      <th>Conflict Events</th>
      <th>National Risk</th>
      <th>Food Security</th>
      <th>Food Price</th>
      <th>Population</th>
      <th>Poverty Rate</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td class="fixed-col">Afghanistan</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="admin1">admin 0, 1</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Burkina Faso</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Cameroon</td>
        <td class="admin0">admin 0</td>
        <td class="admin1">admin 0, 1</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 2</td>
        <td class="admin1">admin 0, 1</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Central African Republic</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 0, 2</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 1, 2</td>
        <td class="admin2">admin 2</td>
        <td class="empty-cell"></td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Chad</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="admin1">admin 1</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 1, 2</td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Colombia</td>
        <td class="admin0">admin 0</td>
        <td class="admin1">admin 0, 1</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Democratic Republic of the Congo</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">El Salvador</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Ethiopia</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Guatemala</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 0, 2</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Haiti</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 0, 2</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Honduras</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 0, 2</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Mali</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Mozambique</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 0, 2</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Myanmar</td>
        <td class="admin0">admin 0</td>
        <td class="admin1">admin 0, 1</td>
        <td class="empty-cell"></td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Niger</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 0, 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 1, 2</td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Nigeria</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 0, 2</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 1, 2</td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">State of Palestine</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="admin1">admin 0, 1</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Somalia</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="empty-cell"></td>
      </tr>
      <tr>
        <td class="fixed-col">South Sudan</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 0, 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="empty-cell"></td>
      </tr>
      <tr>
        <td class="fixed-col">Sudan</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 0, 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="admin1">admin 0, 1</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Syrian Arab Republic</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="empty-cell"></td>
        <td class="empty-cell"></td>
      </tr>
      <tr>
        <td class="fixed-col">Ukraine</td>
        <td class="admin0">admin 0</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="admin1">admin 0, 1</td>
        <td class="admin0">admin 0</td>
      </tr>
      <tr>
        <td class="fixed-col">Venezuela (Bolivarian Republic of)</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 0, 2</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 0, 1, 2</td>
        <td class="empty-cell"></td>
      </tr>
      <tr>
        <td class="fixed-col">Yemen</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 0, 2</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="admin2">admin 2</td>
        <td class="admin0">admin 0</td>
        <td class="empty-cell"></td>
        <td class="admin2">admin 2</td>
        <td class="empty-cell"></td>
        <td class="admin0">admin 0</td>
      </tr>
  </tbody>
</table>
