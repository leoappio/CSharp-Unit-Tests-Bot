using Dell.PPBSys.Entity.Domain;
using Dell.PPBSys.Repository.Contract;
using Dell.PPBSys.Resource;
using NHibernate;
using System.Collections.Generic;
using System.Linq;

namespace Dell.PPBSys.Repository.Implementation
{
    public class InvoiceRepository : Repository<Invoice>, IInvoiceRepository
    {
        public InvoiceRepository(ISession session)
        {
            Session = session;
        }

        public InvoiceRepository() { }

        public IEnumerable<string> FindAllInvoiceNumber(IEnumerable<string> invoiceNumbers)
        {
            var result = Session
                           .CreateSQLQuery(SqlQueries.FindAllInvoiceNumber)
                           .SetParameterList("pInvoiceNumbers", invoiceNumbers)
                           .List<string>();

            return result.ToList();
        }

        public Invoice FindAllInvoiceNumber2(IEnumerable<string> invoiceNumbers, string teste)
        {
            var result = Session
                           .CreateSQLQuery(SqlQueries.FindAllInvoiceNumber)
                           .SetParameterList("pInvoiceNumbers", invoiceNumbers)
                           .List<string>();

            return result.ToList();
        }
    }
}
