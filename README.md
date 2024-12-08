## BBC News Web Scraper

<h3>Overview</h3>

<p>This Python script scrapes articles from the BBC News RSS feed, extracts relevant information and saves the data to an Excel spreadsheet.</p>
<p>It also ensures the RSS feed is valid, includes error handling and provides the user with information as to what is happening during each stage of the process. This helps to visually track the progress of the web scraper and provide context information for any issue the script might run into, if any.</p>
<p>The program is automated tu run at specific times everyday using Windows Task Scheduler and save the article data gotten into a new Excel file with a date stamp.</p>

<h3>Features</h3>
<ul>
  <li>
    Parses the BBC News RSS Feed
  </li>
  <li>
    Extracts this information for each article: 
    <ul>
      <li>
        Title
      </li>
      <li>
        Description
      </li>
      <li>
        Link to the article
      </li>
      <li>
        Date published
      </li>
      <li>
        Thumbnail - if available 
      </li>
    </ul>
  </li>
  <li>
    Saves the data into an Excel spreadsheet with a time and date tag
  </li>
</ul>

<h3>Requirements</h3>

<p>Ensure the following are installed:</p>
<ul>
  <li>
    The latest version of Python
  </li>
  <li>
    Libraries such as:
    <ul>
      <li>
        <em>feedparser</em> - to parse the RSS feed
      </li>
      <li>
        <em>pandas</em> - to structure data into a DataFrame
      </li>
      <li>
        <em>openpyxl</em> - for Excel file support
      </li>
    </ul>
  </li>
</ul>

<h3>Output</h3>

<p>The Excel file is saved with a name like <em>bbc_news_2029_02_13.xlsx</em> and aach row contains the extracted article details.</p>
