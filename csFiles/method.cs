public IEnumerable<string> FindAllInvoiceNumber(IEnumerable<string> invoiceNumbers)
{
    var result = Session
        .CreateSQLQuery(SqlQueries.FindAllInvoiceNumber)
        .SetParameterList("pInvoiceNumbers", invoiceNumbers)
        .List<string>();

    return result.ToList();
}