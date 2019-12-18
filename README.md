# India Bank Search API 🇮🇳
About the Free & Open API: Free to use for all purposes personal/commerical etc.
No authorization at all. No rate limits. I will update data once every few months.

Get Indian Bank's branch information like IFSC, MICR, Exact address, transfer facility information.
Input: Any Indian Bank Name string with an branch-name or address or area of the branch.

The API searches over 150,000 Branches across India and retrieves information like this - 

INPUT: 
```:JSON
{
    "q_bank": "icici",
    "q_branch": "kalkaji market"
}
```


OUTPUT: 
```:JSON
{
    "ADDRESS": "G1 G2 LGF1 BLOCK F1 KALKAJI MAIN MARKET NEW DELHI 19",
    "BANK": "ICICI BANK LIMITED",
    "BRANCH": "KALKAJI MAIN MARKET",
    "CENTRE": "DELHI",
    "CITY": "DELHI",
    "CONTACT": 49875431.0,
    "DISTRICT": "DELHI",
    "IFSC": "ICIC0003993",
    "IMPS": true,
    "MICR": 110229316.0,
    "NEFT": true,
    "RTGS": true,
    "STATE": "DELHI"
}
```

### Endpoint
```https://india-bank-search.sameerkumar.website/api/```

More in Documentation

### Documentation
https://documenter.getpostman.com/view/842558/SWECXvsn

[![Run in Postman](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/842558/SWECXvsn)

#### Data Source
https://github.com/razorpay/ifsc/releases/tag/1.4.9

### Author
Sameer Kumar

https://sameerkumar.website
