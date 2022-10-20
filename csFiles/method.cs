public class BranchRepository{
    public void Evict(Branch obj)
    {
        Session.Evict(obj);   
    }
}