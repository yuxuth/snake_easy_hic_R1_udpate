import gzip


def update_fastq(r1,r2, out_r1,out_r2,barcode_log_file ): ## process two files

    f_out_barcode_log = open(barcode_log_file,"w+")
    f_r1 = gzip.open(r1, 'rt')
    f_r2 = gzip.open(r2, 'rt')
    f_out_r1 = open(out_r1, 'w')
    f_out_r2 = open(out_r2, 'w')
    total_read = 0
    keep_read = 0
    while True:
        cur_r1_name = f_r1.readline().strip()
        cur_r1_read = f_r1.readline().strip()
        cur_r1_plus = f_r1.readline().strip()
        cur_r1_qual = f_r1.readline().strip()
        
        cur_r2_name = f_r2.readline().strip()
        cur_r2_read = f_r2.readline().strip()
        cur_r2_plus = f_r2.readline().strip()
        cur_r2_qual = f_r2.readline().strip()
    
        if cur_r1_read == "" : break
        total_read+=1
        if cur_r1_read.startswith('AGCTT') :
            keep_read+=1
            f_out_r1.write(cur_r1_name+"\n")
            f_out_r1.write(cur_r1_read+"\n")
            f_out_r1.write(cur_r1_plus+"\n")
            f_out_r1.write(cur_r1_qual+"\n")     
        
            f_out_r2.write(cur_r2_name+"\n")
            f_out_r2.write(cur_r2_read+"\n")
            f_out_r2.write(cur_r2_plus+"\n")
            f_out_r2.write(cur_r2_qual+"\n")
    f_r1.close()
    f_r2.close()
    f_out_r1.close()
    f_out_r2.close()
    f_out_barcode_log.write('\n')
    f_out_barcode_log.write('Total reads : %d \n' % total_read)
    f_out_barcode_log.write('keeped reads: %d \n' % keep_read)
    f_out_barcode_log.close()
    

r1 = str(snakemake.input['r1'])
r2 = str(snakemake.input['r2'])
out_r1 = str(snakemake.output['r1'])
out_r2 = str(snakemake.output['r2'])
barcode_log_file = snakemake.output['log']

update_fastq(r1,r2, out_r1,out_r2,barcode_log_file )
