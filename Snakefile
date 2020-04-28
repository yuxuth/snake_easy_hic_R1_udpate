## input the bgi raw fastq file
## extract the 10 or 20 bp barcode from read2, 


shell.prefix("set -eo pipefail; echo BEGIN at $(date); ")
shell.suffix("; exitstat=$?; echo END at $(date); echo exit status was $exitstat; exit $exitstat")

FILES = json.load(open('./samples.json'))
SAMPLES = sorted(FILES.keys())


    

TARGETS = []
final_fq_file_1 = expand("01_fq_r1_update/{sample}_hindIII_filted_L001_R1_001.fastq.gz", sample = SAMPLES)
final_fq_file_2 = expand("01_fq_r1_update/{sample}_hindIII_filted_L001_R2_001.fastq.gz", sample = SAMPLES)
TARGETS.extend(final_fq_file_1)
TARGETS.extend(final_fq_file_2)

rule all:
    input: TARGETS

rule extract_index_fq:
    input : 
        r1 = lambda wildcards: FILES[wildcards.sample]['R1'],
        r2 = lambda wildcards: FILES[wildcards.sample]['R2']
    output:
        r1= ("01_fq_r1_update/{sample}_hindIII_filted_L001_R1_001.fastq"), 
        r2= ("01_fq_r1_update/{sample}_hindIII_filted_L001_R2_001.fastq"),
        log = "02_info/{sample}.filter_log"
    script:
        "scripts/each_hic_fq_update.py"
        
rule gzip_r1:  
    input : "01_fq_r1_update/{sample}_hindIII_filted_L001_R1_001.fastq"
    output: "01_fq_r1_update/{sample}_hindIII_filted_L001_R1_001.fastq.gz"
    shell: 
        """
        gzip {input}
        """
rule gzip_r2:  
    input : "01_fq_r1_update/{sample}_hindIII_filted_L001_R2_001.fastq"
    output: "01_fq_r1_update/{sample}_hindIII_filted_L001_R2_001.fastq.gz"
    shell: 
        """
        gzip {input}
        """
