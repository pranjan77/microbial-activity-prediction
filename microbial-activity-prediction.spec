/*
A KBase module: microbial-activity-prediction
*/

module microbial-activity-prediction {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_microbial-activity-prediction(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
