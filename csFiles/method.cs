public class InvoiceRepository{
    public IEnumerable<PPidTeste> FindAllInvoiceNumber(IEnumerable<string> invoiceNumbers)
    {
        var result = Session
            .CreateSQLQuery(SqlQueries.FindAllInvoiceNumber)
            .SetParameterList("pInvoiceNumbers", invoiceNumbers)
            .List<PPidTeste>();

        return result.ToList();
    }
}