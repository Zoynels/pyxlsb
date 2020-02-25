def to_dataframe(sheet, skiprows=None, header=0, nrows=None, header_string=False):
    """
    Example of convertation of sheet values to pandas.DataFrame
    """
    import pandas as pd

    header_list = []
    df_list = []
    
    for i_row, row in enumerate(sheet.rows()):
        if (header is not None) and (i_row == header):
            for cell in row:
                if header_string:
                    header_list.append(cell.value_conv)
                else:
                    header_list.append(str(cell.value_conv))
            continue
            
        if (skiprows is not None) and (skiprows > 0):
            skiprows -= 1
            continue

        if nrows is not None:
            if nrows > 0:
                nrows -= 1
            else:
                break
        
        body_list = []
        for cell in row:
            body_list.append(cell.value_conv)
        df_list.append(pd.DataFrame([body_list]))

    if len(df_list) == 0:
        return None

    df = pd.concat(df_list, axis=0, ignore_index=True)
    if len(header_list) != 0:
        try:
            df.columns = header_list
        except Exception as e:
            raise ValueError(e)
    return df
