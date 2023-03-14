def get_status(res_privat):
    '''
    Description displays the status code to get information from the api bank

    Parameters
    ----------
        res_privat : the variable contains a dictionary with currency data

    Returns
    -------
    The information about the status code
    '''
    return print(f"\nStatus code: {res_privat.status_code}\n")
