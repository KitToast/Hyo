import requests
import bs4
import os

class arxivFetcher:
	"""Object responsible for communicating with web server and fetching necessary materials"""

	def __init__(self, arxivcode):

		#Set arxiv identifier code
		self.arxivcode = arxivcode

		#Set relevant BeautifulSoup object for information retrival
		self.soupObj = bs4.BeautifulSoup(requests.get('https://www.arxiv.org/abs/' + arxivcode).text)
 		

		
	#Traverses tree to find title
	def fetchTitle():
		
		return list(self.soupObj.findall('h1')[2],children)[1:]

	#Returns a list of author strings
	def fetchAuthors():

			authorList = list()

			for authorLink in (self.soupObj).find("div",class_="authors").contents:

				if(authorLink.name == 'a'):
					authorList.add(authorLink.contents[0])

			return authorList

	#Returns a list of strings of relevant subjects
	def fetchSubjects():

		contents  = soupObj.find("td",class_="tablecell subjects")

		return (contents[0].contents, contents[1:])

	#Returns Request object with relevant pdf from arXiv repo
	def fetchPDF():
		
		return requests.get('https://www.arxiv.org/pdf/' + self.arxivcode + '.pdf')



#Object created to handle file construction and directory organization
class FileManager:

	#Initialize File Manager
	def __init__(self, arxivFetcher fetcher):
		self.fetcher = fetcher

		self.paper_title = fetcher.fetchTitle()

		#We will only consider the first name of the paper for now
		self.primary_author = fetcher.fetchAuthors

		self.primary_subject , _ = fetcher.getSubjects

		relevant_directory = os.path.join('~/Papers' , self.primary_subject , self.primary_author) 
		
		if(not os.path.exists(relevant_directory)):
			os.makedirs(relevant_directory)


		self.path = os.path.join(relevant_directory, self.paper_title + ".pdf")

	#Saves PDF to specified location. The directory hierarchy goes as follows: path/primary_subject,first_author,paper_title.pdf
	def savePDF():

		writeFile = open(self.path,"wb")

		#Use rudimenatary chunk write from request for now 
		chunk_iter = (fetcher.fetchPDF()).
		for chunks in chunk_iter.iter_content(20000):
			writeFile.write(chunks)

		writeFile.close()

	def doesExist():
		
		return os.path.exists(self.path)		


def main():

	test = arxivFetcher('1808.00937')
	print(test.fetchTitle())
	print(test.fetchAuthors())
	print(test.fetchSubjects())
