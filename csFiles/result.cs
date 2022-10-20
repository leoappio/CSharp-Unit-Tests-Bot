[TestMethod]
public void None()
{
    //Arrange
    var session = Substitute.For<ISession>();
    var branchRepository = new BranchRepository(session);

    var branchId = 22222;

    var expectedResult = new Branch();

    _ = session.Load<Branch>(branchId).ReturnsForAnyArgs(expectedResult);   

    //Act
     var result = branchRepository.Load(branchId);

    //Assert
    using (new AssertionScope())
    {
        _ = result.Should().BeEquivalentTo(expectedResult);
    }
}
