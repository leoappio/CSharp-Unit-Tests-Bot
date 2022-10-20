[TestMethod]
public void EvictingShouldBeExecutedSuccessfully()
{
    //Arrange
    var session = Substitute.For<ISession>();
    var branchRepository = new BranchRepository(session);

    var obj = new Branch();

    //Act
     var result = branchRepository.Evict(obj);

    //Assert
    using (new AssertionScope())
    {
        _ = session.Received().Evict(Arg.Any<Branch>());
    }
}
