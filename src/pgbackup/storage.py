
def local(infile, outfile):
    """Backup database locally. 
       This takes what in the 'infile' and returns writes it to the 'outfile'"""
    outfile.write(infile.read)
    outfile.close()
    infile.close()


def s3(client, infile, bucket, name):
    """This method takes an AWS client object that has a 'upload_file' method as 'client', 
    a file object with the data from postgresql backup as 'infile', the bucket name as 'bucket', and
    lastly the name of the file you would like to cerate in your s3 bucket as 'name'   """
    client.upload_fileobj(infile, bucket, name)
