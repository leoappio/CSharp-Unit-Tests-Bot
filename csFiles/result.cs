[TestMethod]
public void FindingAllInvoiceNumberShouldReturnList()
{
    //Arrange
    var session = Substitute.For<ISession>();
    var invoiceRepository = new InvoiceRepository(session);

    var invoiceNumbers = new List<string>
    {
        "AAA"
    };

    var expectedResult = new List<PPidTeste>
    {
        new PPidTeste()
    };

    _ = session
        .CreateSQLQuery(SqlQueries.FindAllInvoiceNumber)
        .SetParameterList("pInvoiceNumbers", invoiceNumbers)
        .List<PPidTeste>().ReturnsForAnyArgs(expectedResult);

    //Act
     var result = invoiceRepository.FindAllInvoiceNumber(invoiceNumbers);

    //Assert
    using (new AssertionScope())
    {
        _ = result.Should().BeEquivalentTo(expectedResult);
    }
}
