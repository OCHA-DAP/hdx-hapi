
# Data Coverage

---

The initial aim of HDX HAPI is to cover all countries that have a
humanitarian response plan, and all data sub-categories from
[HDX data grids](https://data.humdata.org/dashboards/overview-of-data-grids).
In the table below we detail the sub-category coverage that we have achieved
at present, and to which administrative level: country, admin 1, or admin 2.

<style>
  table {
    border-collapse: separate;
    width: 100%;
  }

  th, td {
    padding: 8px 12px;
    border-right: 1px solid #CCC;
    white-space: nowrap;
    min-width: 200px;
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
    height: 200px;
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
	}
</style>

  <table>
    <thead>
      <tr>
        <th class="fixed-col"></th>
          <th>Humanitarian Needs</th>
          <th>Refugees</th>
          <th>Conflict event</th>
          <th>Funding</th>
          <th>National Risk</th>
          <th>Operational Presence</th>
          <th>Food Price</th>
          <th>Food Security</th>
          <th>Population</th>
          <th>Poverty-rate</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="fixed-col">Afghanistan</td>
        <td>foo</td>
        <td>foo</td>
        <td>foo</td>
        <td>foo</td>
        <td>foo</td>
        <td>foo</td>
        <td>foo</td>
        <td>foo</td>
        <td>foo</td>
        <td>foo</td>
      </tr>
	    <tr>
	      <td class="fixed-col">Burkina Faso</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	    </tr>
	    <tr>
	      <td class="fixed-col">Cameroon</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	    </tr>
	    <tr>
	      <td class="fixed-col">Central African Republic</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	      <td>foo</td>
	    </tr>
    </tbody>
  </table>