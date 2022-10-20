public class BranchRepository{
    public Branch Load(long? branchId)
    {
        return Session.Load<Branch>(branchId);   
    }
}