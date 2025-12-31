package com.hackathon.sentiment.dto;

import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * DTO: Response received from FastAPI ML service
 * Maps fields from Spanish (FastAPI) to Java variables
 */
public record FastApiResponse(

    @JsonProperty("prevision")
    String prevision,

    @JsonProperty("probabilidad")
    Double probabilidad,

    @JsonProperty("timestamp")
    String timestamp
) {}
