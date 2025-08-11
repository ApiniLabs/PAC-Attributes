### `valid_until`
- provide `valid_until`, even when the value is small. Choose a value in the order of magnitude it takes for a value to realistically become obsolete. 
Reason: In many cases a new value needs to be propagated through multiple systems / organisational units. Setting ValidUntil to the same order of magnitude it takes to reach eventual consistency or maybe an order lower will reduce the number of meaningless requests. requests, while keeping the 




It is the `Attribute Client`s responsibility to present this in a way, which is meaningful to their users. The `Attribute Service` is MUST not pre-filter. (BEST PRACTICE for library implementation on client side: The library should not filter either, as it typically lacks the context to judge the importance and reliability. ) 


It is RECOMMENDED the client presents the attribute groups in order of the CITs (assuming CITs are ordered by importance)



## Implementation Considerations for Libraries
<div style="color:red"> Note, that this application will usually have a functionality which goes beyond what is specified here. Conversely, a library implementing an `Attribute Client` would typically not implement the entire specification but focus on the generic parts and provide means for applications to inject databases etc.

On client side there are two levels of concern: 
1. attribute client library,  which knows about the details of attributes, typically implemented in the form of a library
2. an app, which makes use of attributes for interactions with the environment (e.g. user)

The app typically provides infrastructure such as databases etc. Thus long term caching (would need database) cannot solely be handled by the attribute client. Additionally, the app knows more about it’s context and might need to implement a custom caching strategy (there might be scenarios, where higher or lower update frequency is necessary).
Thus the attribute client (especially if a library) should:

- implement an in memory cache as default
- provide means for the app to inject a storage for caching (e.g. database or file)
- provide means for the app to inject a custom caching logic
</div>
