package com.hackathon.sentiment.dto;

/**
 * DTO: Request to send to FastAPI ML service
 * Maps to FastAPI endpoint POST /predict
 */
public record FastApiRequest(
    String text
) {}
