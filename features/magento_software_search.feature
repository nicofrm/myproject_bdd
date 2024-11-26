Feature: If the user searches for a product, proper results must be returned according
      to the search criteria and filters

    @T1
    Scenario: Verify that when the user searches for a keyword, the search returns results according to that keyword
        Given I am on magento software testing homepage
        When I click on the search input and I enter "capri" text
        When I click "ENTER"
        Then I should have at least "1" results returned
        Then The search results should have "capri" in the product title


