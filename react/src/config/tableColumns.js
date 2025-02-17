export const expenseColumns = [
    {
        id: 'date',
        label: 'Date',
        render: (expense) => new Date(expense.Date).toLocaleDateString()
    },
    {
        id: 'description',
        label: 'Description',
        render: (expense) => expense['Expense Name']
    },
    {
        id: 'category',
        label: 'Category',
        render: (expense) => expense['Budget Category']
    },
    {
        id: 'account',
        label: 'Account',
        render: (expense) => expense['Account Number']
    },
    {
        id: 'amount',
        label: 'Amount',
        render: (expense) => `$${Math.abs(expense.Amount).toFixed(2)}`
    }
]; 