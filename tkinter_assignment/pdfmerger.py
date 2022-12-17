import logging
from PyPDF2 import PdfMerger

try:
    
    def pdfmerger(pdflist,pdfname):
        """This function accepts a list of PDFs and merges them in the name which is accepted as the second argument.
        parameters
                    : pdflist - files in the form of any iterable 
                    : pdfname - The name for the output file in str """
        
        
        merger=PdfMerger()
        for i in pdflist:
            merger.append(i)
        name=pdfname+'.pdf'
        merger.write(name)
        merger.close()
        return name

except Exception:
    
    logger=logging.getLogger(__name__)
    Handler=logging.FileHandler('pdfmerger.log')
    Format=logging.Formatter('%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s',datefmt='%d/%m/%Y  %I:%M:%S %p')
    Handler.setFormatter(Format)
    logger.addHandler(Handler)

    logger.exception('Unexpected Exception occured while merging PDFs.')
    